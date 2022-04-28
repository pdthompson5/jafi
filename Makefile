
.PHONY: jafi
jafi:
	python jafi

.PHONY: gen_ast
gen_ast: 
	python gen_ast/gen_ast.py

.PHONY: jafi_debug
jafi_debug:
	python jafi debug

.PHONY: jafi_info
jafi_info:
	python jafi info 


.PHONY: jafi_interactive
jafi_interactive:
	python jafi_interactive

.PHONY: test
test:
	python -m pytest tests/*

.PHONY: clean
clean:
	-rm jafi/*.pyc
	-rm -r .pytest_cache