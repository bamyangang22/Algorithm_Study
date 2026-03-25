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
    """노션 데이터베이스에 이미 해당 제목의 문제가 있는지 확인합니다."""
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    # 제목(Name) 속성을 기준으로 동일한 텍스트가 있는지 필터링하여 쿼리
    filter_data = {
        "filter": {
            "property": "Name", 
            "title": { "equals": title }
        }
    }
    response = requests.post(url, headers=headers, json=filter_data)
    if response.status_code == 200:
        return len(response.json().get("results")) > 0
    return False

def parse_readme(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 제목 추출 로직 ([level 1] 폰켓몬 - 1845 -> "폰켓몬")
        title_match = re.search(r'\]\s*(.*?)\s*-', content)
        title = title_match.group(1).strip() if title_match else None
        if not title: return None
        
        level_match = re.search(r'level\s*(\d+)', content)
        level = f"Lv.{level_match.group(1)}" if level_match else "알 수 없음"
        
        type_match = re.search(r'구분\n\n.*?>\s*(.*)', content)
        problem_type = type_match.group(1).strip() if type_match else "분류 없음"

        platform = file_path.split('/')[0]

        return {
            "title": title,
            "level": level,
            "platform": platform,
            "type": problem_type,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    except Exception as e:
        print(f"파일 파싱 에러 ({file_path}): {e}")
        return None

def upload_to_notion(data):
    if not data: return
    
    # 1. 중복 확인: 이미 노션에 있는 문제라면 건너뜁니다.
    if check_if_exists(data['title']):
        print(f"이미 노션에 존재함: {data['title']} (건너뜁니다)")
        return

    # 2. 존재하지 않을 때만 새로 생성
    payload = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Name": { "title": [{ "text": { "content": data['title'] } }] },
            "플랫폼": { "select": { "name": data['platform'] } },
            "문제 난이도": { "select": { "name": data['level'] } },
            "문제 유형": { "multi_select": [{"name": data['type']}] },
            "풀이 날짜": { "date": { "start": data['date'] } },
            "풀이 상태": { "status": { "name": "✅완료" } }
        }
    }
    res = requests.post("https://api.notion.com/v1/pages", json=payload, headers=headers)
    if res.status_code == 200:
        print(f"신규 등록 완료: {data['title']}")
    else:
        print(f"등록 실패: {res.text}")

if __name__ == "__main__":
    for root, dirs, files in os.walk("."):
        # .github 폴더나 숨김 폴더는 제외하여 성능 최적화
        if ".github" in root or ".git" in root:
            continue
            
        if "README.md" in files:
            path = os.path.join(root, "README.md")
            data = parse_readme(path)
            if data:
                upload_to_notion(data)
