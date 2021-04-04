# restful-api
basic restful-api server 

##**ana proje**
Server içerisine SQLALCHEMY ile bir database kurulmuştur.
Database içerisinde 3 adet veri vardır.(video/1, video/2, video/3)
main.py çalıştırıldıktan sonra test.py üzerinden 4 endpointe istek atılarak çalıştırılır.
Server 4 tane endpoint tutuyor bunlar, GET,PUT,PATCH ve DELETE.Örneğin:
              localhost:5000/video/1
 ##**KAFKA**
Kafka producer 3 saniyede bir log dosyasına giden istekleri topluyor ve kafka managera iletiyor oradan consumer toplayarak consumer.txt dosyasına ve dosya oradan database e kaydediliyor.
Kafkayı çalıştırmak için:
-kafka_2.13-2.7.0$ bin/zookeeper-server-start.sh config/zookeeper.properties
-kafka/CMAK/target/universal/cmak-3.0.0.5$bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080
-kafka_2.13-2.7.0$ JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties
-localhost:8080
##**DOCKER**
Docker-compose için:
-docker build -t flask-docker 
-docker run -d -p 80:5000 flask-docker
-docker desktop da images kısmında gözükür ve açılır.
-localhost:80




anahtar kod:gAAAAABgUI-kRflkLOsVTD_a51XV9cyziHvm-Uie1eW6mt94BNBkiGE0DR0_LS1KL0adCdfklLwKD92QXUdy9t64U6bibrhJGwd33SlsHq6Et2ZLnQvtMIt7S12gP0RQlzPohqA3ohx9x4qe0g2qRhhYvJRLsaNFaAnN5sw3XP8glBjrLI9DpEnYqqZmqIpmq5d9l67F_ggV
