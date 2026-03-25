# sync_to_notion.py 파일의 upload_to_notion 함수 내부를 수정하세요.

def upload_to_notion(data):
    if not data: return
    
    if check_if_exists(data['title']):
        print(f"이미 존재함: {data['title']}")
        return

    payload = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            # "Name"이었던 부분을 "문제 이름"으로 변경!
            "문제 이름": { "title": [{ "text": { "content": data['title'] } }] }, 
            "플랫폼": { "select": { "name": data['platform'] } },
            "문제 난이도": { "select": { "name": data['level'] } },
            "문제 유형": { "multi_select": [{"name": data['type']}] },
            "풀이 날짜": { "date": { "start": data['date'] } },
            "풀이 상태": { "status": { "name": "✅완료" } }
        }
    }
    # ... 이하 동일
