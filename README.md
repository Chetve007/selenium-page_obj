Autotest web project, with tools and instruments: pytest, selenium, page object (pattern)

Command for launch main test:
`pytest -v --tb=line --language=en tests/test_main_page.py`

Comand for launch tests for review:
`pytest -v --tb=line --language=en -m need_review`