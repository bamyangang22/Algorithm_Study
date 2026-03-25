import os, re, requests
from datetime import datetime

# 깃허브 Secrets에서 가져온 환경변수
NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def parse_readme(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. 제목 및 번호 추출: [level 1] 폰켓몬 - 1845 -> "폰켓몬"
        title_match = re.search(r'\]\s*(.*?)\s*-', content)
        title = title_match.group(1).strip() if title_match else "제목 없음"
        
        # 2. 난이도 추출: [level 1] -> "Lv.1"
        level_match = re.search(r'level\s*(\d+)', content)
        level = f"Lv.{level_match.group(1)}" if level_match else "알 수 없음"
        
        # 3. 유형 추출: 코딩테스트 연습 > 해시 -> "해시"
        type_match = re.search(r'구분\n\n.*?>\s*(.*)', content)
        problem_type = type_match.group(1).strip() if type_match else "분류 없음"

        # 4. 플랫폼: 폴더 구조에서 추출 (예: 프로그래머스/lv1/...)
        platform = file_path.split('/')[0]

        return {
            "title": title,
            "level": level,
            "platform": platform,
            "type": problem_type,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    except Exception as e:
        print(f"파일 파싱 에러: {e}")
        return None

def upload_to_notion(data):
    if not data: return
    
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
        print(f"성공: {data['title']}가 노션에 등록되었습니다.")
    else:
        print(f"실패: {res.text}")

# 메인 실행부: 새로 추가된 README.md만 찾아서 실행
if __name__ == "__main__":
    for root, dirs, files in os.walk("."):
        if "README.md" in files:
            path = os.path.join(root, "README.md")
            # 너무 오래된 파일은 건너뛰고 싶다면 로직 추가 가능
            print(f"처리 중: {path}")
            data = parse_readme(path)
            upload_to_notion(data)
