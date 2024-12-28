def process_paragraphs(text):
    # 문단을 줄바꿈으로 구분
    paragraphs = text.split('\n')
    
    # 각 문단에 따옴표를 추가하고 4칸 들여쓰기 적용, '#'으로 시작하는 문단은 제외
    processed_paragraphs = []
    for paragraph in paragraphs:
        stripped_paragraph = paragraph.strip()
        if stripped_paragraph and not stripped_paragraph.startswith('#'):  # 빈 문단과 '#'으로 시작하는 문단은 제외
            # 시작과 끝에 작은 따옴표 또는 큰 따옴표가 있으면 제거
            while stripped_paragraph.startswith(("'", '"')):
                stripped_paragraph = stripped_paragraph[1:]
            while stripped_paragraph.endswith(("'", '"')):
                stripped_paragraph = stripped_paragraph[:-1]
            
            # 큰 따옴표로 감싸지지 않은 경우만 따옴표 추가
            stripped_paragraph = '"' + stripped_paragraph + '"'
            processed_paragraph = '    ' + stripped_paragraph
            processed_paragraphs.append(processed_paragraph)
    
    # 문단을 다시 합쳐서 반환
    return '\n'.join(processed_paragraphs)

# """ 시나리오 입력 """
input_text = """여기에 시나리오 복사"""

# 변환된 텍스트 출력
output_text = process_paragraphs(input_text)
print(output_text)