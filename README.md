# MQTT-UWBsender
 Envio e recebimento de mensagens UWB utilizando o protocólo MQTT.

A pasta possui dois arquivos Python: 'publishUWB.py' e 'subscribeUWB.py'.
publishUWB simula mensagens UWB de forma aleatória e publica no tópico "UWB" do broker público "test.mosquitto.org".
subscribeUWB acessa o tópico "UWB" e armazena os dados recebidos em dois arquivos de texto. Em um arquivo é armazenado
em sintaxe de dicionário e no outro em formato de tabela.

Os dois programas devem ser rodados simultaneamente. publishUWB envia 10 dados e pára, por isso subscribeUWB deve
ser incializado antes para acessar todos. subscribeUWB poderia ser generalizado para recebimento contínuo e por isso
precisa ser parado depois de guardar as 10 mensagens.

Pacotes utilizados: paho-mqtt, json, random, time.
