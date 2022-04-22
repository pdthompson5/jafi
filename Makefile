
.PHONY: jafi
jafi:
	python3 jafi

.PHONY: jafi_interactive
jafi_interactive:
	python3 jafi_interactive

.PHONY: test
test:
	pytest tests/*

.PHONY: clean
clean:
	-rm jafi/*.pyc