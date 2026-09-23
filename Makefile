.PHONY: test status new lint challenge challenges ladder

test:
ifdef m
	pytest modules/m$(m)*/tests -v
else
	pytest modules -q
endif

new:
	@python tools/new_module.py --tier $(t) --topic $(topic)

status:
	@python tools/status.py

lint:
	ruff check modules tools

challenge:
	pytest challenges/phase-$(p)*/$(s)*/tests -v

challenges:
	pytest challenges -q

ladder:
	@python tools/challenges.py
