# Nagios check Volt POP Protect

This plugin can test all Fiberhome pon slot with 8 or 16 PONs if PON link status is UP or DOWN

The plugin check if in all PONs of a specific SLOT has customers, if a PON port have one or more customers and PON status is DOWN one alarm is generated.

---
#### Nagios check PON in OLT Fiberhome <br>
Written by Jorge Luiz Taioque <br>
This plugin check status of a PON Slot connected in a specific OLT  <br>
and return if these PON operational state is UP or DOWN <br>


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
