<!DOCTYPE html>
<html lang = "en">

<!--
    < Head tag>

    문서의 메타 데이터 저장 공간
    메타 데이터 : 데이터에 대한 데이터
                 제목, 스타일, 저자정보, 링크 등
-->

<head>
    <title>Document</title>
</head>

<!--
    < Body tag>

    HTML의 시각적인 부분을 담는 공간
    다양한 태그를 통하여 페이지 구성

    < hn tag >   -> n은 숫자

    문서 내 제목을 표현할 때 사용
    H1 ~ H6 tag로 구성되며 1이 가장 큰 제목, 6이 가장 작은 제목
    줄간격 띄움과 굵은 글자 효과가 적용됨

    < p tag >
    
    본문을 나타내기 위한 태그로서 문단 하나를 생성함
    <p> 태그 내 본문 안의 불필요한 공백들은 적용되지 않음

    < br tag >

    줄바꿈을 수행하기 위한 태그

    < hr tag >

    수평줄 삽입을 위한 태그
    문서 구조의 명확한 구분을 나타내기 위해 활용

    < pre tag >

    문자열들이 입력된 상태 그대로 화면에 출력하기 위한 태그
    <p> 태그에서는 무시되던 공백 문자들 (빈칸, 탭, 줄바꿈 등) 이 그대로 유지되어 출력됨

    <ul>

    순서가 없는 리스트를 표현하기 위한 태그
    리스트의 각 항목 : <li> 태그를 사용하여 표기
    <ul style = "list-style-type : [블릿모양]"> ... </ul>
    블릿모양 : disc -> 기본형식으로 표기 (검은색 원)
              circle -> 원형 표기 (흰색 원)
              square -> 정사각형 표기 (검은색 네모)
              none -> 표기하지 않음

    < ol tag >

    순서가 있는 리스트를 표현하기 위한 태그
    리스트의 각 항목 : <li> 태그를 사용하여 표기
    <ol type = "순서 표기 형식"> ... </ol>
    순서 표기 형식 : 1 -> 기본 형식으로 표기(숫자)
                    A -> 대문자로 표기
                    a -> 소문자로 표기
                    I -> 대문자 로마 숫자 표기
                    i -> 소문자 로마 숫자 표기

    < dl tag >

    이름과 설명으로 구성되는 항목들의 리스트를 표기하기 위한 태그
    리스트의 각 항목 : <dt> 태그 -> 항목의 이름
                      <dd> 태그 -> 항목에 대한 설명

    < 중첩 리스트 >

    리스트 안에 또 다른 리스트를 포함할 수 있음

    < table tag >

    표 형태로 데이터를 표현하기 위한 태그
    <tr> : 행을 나타내는 태그
    <th> : 제목 셀을 나타내는 태그
    <td> : 일반적인 데이터 셀을 나타내는 태그
    <table border = "1"> : Table 태그에 border 속성 추가
        0 -> 경계선 없음
        1 -> 경계선 사용
        HTML5 표준에서 제외된 예전 기능
    
    < CSS 적용 Table >

    경계선 -> border:width style color  ex) border : 2px dotted red;
    경계선 합치기 -> border-collapse: border model   ex) border-collapse: collapse;
    글자 정렬 -> text-align: align method   ex) text-align:center;
    
    < 테이블 의미구조 tag >

    <caption> -> 테이블의 제목
    <thead> -> 테이블의 머리말
    <tbody> -> 테이블의 본문
    <tfoot> -> 테이블의 꼬리말
        
-->

<body>
    <h1>Hello, hehe World</h1>
    <h2>haha</h2>
    <h3>small</h3>
    <p>Great!</p>
    <hr/>
    <p>First Sentence<br/>Second Sentence</p>
    <pre>
        p태그를
        이용하면
        줄간격
        띄움
        효과가         발생합니다
    </pre>
</body>

</html>
