.PHONY: test status new lint

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
