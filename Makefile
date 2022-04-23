
.PHONY: jafi
jafi:
	python3 jafi

.PHONY: jafi_debug
jafi_debug:
	python3 jafi debug

.PHONY: jafi_info
jafi_info:
	python3 jafi info 


.PHONY: jafi_interactive
jafi_interactive:
	python3 jafi_interactive

.PHONY: test
test:
	pytest tests/*

.PHONY: clean
clean:
	-rm jafi/*.pyc