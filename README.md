# Nagios check Volt POP Protect

Os plugins para nagios realizam leitura nos equipamentos Volt POPProtect para vários sensores como:
* Alarme ativo
* Entrada AC
* Voltagem de Entrada
* Voltagem das Baterias
* Temperatura Interna
* Temperatura do sensor externo

![http://www.volt.ind.br/popprotect.php](https://github.com/jorgeluiztaioque/lxd-forward/blob/master/lxd.png?raw=true)
---
#### Nagios check Volt POPProtect <br>
Written by Jorge Luiz Taioque <br>

### Dependencias
<pre>
apt install python3
apt install python3-pip
apt install libsnmp-dev snmp-mibs-downloader
apt install gcc python3-dev
pip3 install easysnmp
</pre>
----- <br>
### Uso: <br>
./check_nome_plugin [IP_POP_PROTEC] [ARGUMENTOS se ouver] <br>
Exemplo: <br>
./check_nome_plugin 10.10.10.1 10 <br>
Apenas utilize argumentos se é necesário para o plugin <br>
<br>
Para configurar no nagios service.cfg use: <br>
check_command:	check_pon_fiberhome!10.10.10.1!1 <br>


### Configuração no nagios
Inserir as linhas no arquivo nagios command.cfg use:<br>
define command{<br>
        command_name    check_nome_do_plugin<br>
        command_line    $USER1$/check_nome_do_plugin $ARG1$ $ARG2$ #argumentos se necessário<br>
        }<br>
