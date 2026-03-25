import os, re, requests
from datetime import datetime

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def check_if_exists(title):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    filter_data = {"filter": {"property": "문제 이름", "title": {"equals": title}}}
    response = requests.post(url, headers=headers, json=filter_data)
    if response.status_code == 200:
        return len(response.json().get("results")) > 0
    return False

def parse_readme(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 제목 추출 ([level 1] 폰켓몬 - 1845 -> "폰켓몬")
        title_match = re.search(r'\]\s*(.*?)\s*-', content)
        title = title_match.group(1).strip() if title_match else None
        if not title:
            print(f"   ⚠️ 제목 추출 실패: {file_path}")
            return None
        
        level_match = re.search(r'level\s*(\d+)', content)
        level = f"Lv.{level_match.group(1)}" if level_match else "알 수 없음"
        
        # 문제 유형 추출 (구분 아래줄에서 추출)
        type_match = re.search(r'구분\s*\n\s*\n.*?>\s*(.*)', content)
        problem_type = type_match.group(1).strip() if type_match else "분류 없음"

        platform = file_path.split(os.sep)[1] if os.sep in file_path else "기타"

        return {
            "title": title, "level": level, "platform": platform,
            "type": problem_type, "date": datetime.now().strftime("%Y-%m-%d")
        }
    except Exception as e:
        print(f"   ❌ 파일 분석 중 에러: {e}")
        return None

def upload_to_notion(data):
    if not data: return
    if check_if_exists(data['title']):
        print(f"   ⏭️ 이미 존재함: {data['title']}")
        return

    payload = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "문제 이름": { "title": [{ "text": { "content": data['title'] } }] },
            "플랫폼": { "select": { "name": data['platform'] } },
            "문제 난이도": { "select": { "name": data['level'] } },
            "문제 유형": { "multi_select": [{"name": data['type']}] },
            "풀이 날짜": { "date": { "start": data['date'] } },
            "풀이 상태": { "status": { "name": "✅완료" } }
        }
    }
    res = requests.post("https://api.notion.com/v1/pages", json=payload, headers=headers)
    if res.status_code == 200:
        print(f"   ✅ 신규 등록: {data['title']}")
    else:
        print(f"   ❌ 노션 API 에러: {res.text}")

if __name__ == "__main__":
    print(f"🚀 동기화 시작 (경로: {os.getcwd()})")
    count = 0
    for root, dirs, files in os.walk("."):
        if ".github" in root or ".git" in root or root == ".": continue
        
        for file in files:
            if file.upper() == "README.MD": # 대소문자 무관하게 탐색
                path = os.path.join(root, file)
                print(f"📂 발견: {path}")
                data = parse_readme(path)
                if data:
                    upload_to_notion(data)
                    count += 1
    print(f"🏁 종료 (총 {count}개 처리됨)")
