# This is an example based in Java. You can change it to the language/runtime you are using

FROM openjdk:11

COPY api/build/libs/api.jar /api.jar

CMD ["java", "-jar", "/api.jar"]

EXPOSE 8080
