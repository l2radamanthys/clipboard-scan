comandos:
	@echo ""
	@echo "iniciar"
	@echo "ejecutar"
	@echo "detener"
	@echo ""


clear:
	@pipenv run python reader.py -clear

clear-config:
	@pipenv run python reader.py -clearconfig

ejecutar:
	@pipenv run python reader.py
run:
	@pipenv run python reader.py
