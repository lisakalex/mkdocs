Below is a working **Jenkinsfile** pattern.

Mule Maven Plugin supports packaging/deployment through Maven lifecycle, and MuleSoft documents deployment via
`mvn ... -DmuleDeploy`. Jenkins `withCredentials` safely exposes secrets as environment
variables. ([MuleSoft Documentation][1]) ([MuleSoft Documentation][2]) ([Jenkins][3])

```groovy
pipeline {
    agent any

    tools {
        maven 'Maven-3.9'
        jdk 'JDK-17'
    }

    parameters {
        choice(name: 'ENVIRONMENT', choices: ['dev', 'test', 'prod'], description: 'Target environment')
        string(name: 'APP_NAME', defaultValue: 'my-mule-api', description: 'CloudHub app name')
        string(name: 'MULE_VERSION', defaultValue: '4.6.0', description: 'Mule runtime version')
    }

    environment {
        ANYPOINT_URI = 'https://anypoint.mulesoft.com'
        BUSINESS_GROUP = 'My Business Group'
        REGION = 'eu-west-1'
        WORKERS = '1'
        WORKER_TYPE = 'MICRO'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                sh '''
                    mvn clean test
                '''
            }
        }

        stage('Deploy to Anypoint') {
            steps {
                withCredentials([
                        usernamePassword(
                                credentialsId: 'anypoint-username-password',
                                usernameVariable: 'ANYPOINT_USERNAME',
                                passwordVariable: 'ANYPOINT_PASSWORD'
                        ),
                        string(
                                credentialsId: 'mule-secret-key',
                                variable: 'MULE_SECRET_KEY'
                        )
                ]) {
                    sh '''
                        set +x

                        mvn clean deploy -DmuleDeploy \
                          -Danypoint.username="$ANYPOINT_USERNAME" \
                          -Danypoint.password="$ANYPOINT_PASSWORD" \
                          -Danypoint.uri="$ANYPOINT_URI" \
                          -Dbusiness.group="$BUSINESS_GROUP" \
                          -Denv="$ENVIRONMENT" \
                          -Dapp.name="$APP_NAME-$ENVIRONMENT" \
                          -Dmule.version="$MULE_VERSION" \
                          -Dregion="$REGION" \
                          -Dworkers="$WORKERS" \
                          -Dworker.type="$WORKER_TYPE" \
                          -Dsecret.key="$MULE_SECRET_KEY"
                    '''
                }
            }
        }
    }
}
```

Example `pom.xml` parameter usage:

```xml

<plugin>
    <groupId>org.mule.tools.maven</groupId>
    <artifactId>mule-maven-plugin</artifactId>
    <version>${mule.maven.plugin.version}</version>
    <extensions>true</extensions>

    <configuration>
        <cloudHubDeployment>
            <uri>${anypoint.uri}</uri>
            <muleVersion>${mule.version}</muleVersion>
            <username>${anypoint.username}</username>
            <password>${anypoint.password}</password>
            <applicationName>${app.name}</applicationName>
            <environment>${env}</environment>
            <businessGroup>${business.group}</businessGroup>
            <region>${region}</region>
            <workers>${workers}</workers>
            <workerType>${worker.type}</workerType>

            <properties>
                <secret.key>${secret.key}</secret.key>
            </properties>
        </cloudHubDeployment>
    </configuration>
</plugin>
```

In Jenkins, create credentials:

```text
anypoint-username-password  -> Username with password
mule-secret-key             -> Secret text
```

Main command being run:

```bash
mvn clean deploy -DmuleDeploy -Dsecret.key="$MULE_SECRET_KEY"
```

[1]: https://docs.mulesoft.com/mule-runtime/latest/mmp-concept?utm_source=chatgpt.com "Mule Maven Plugin"

[2]: https://docs.mulesoft.com/cloudhub-2/ch2-deploy-maven?utm_source=chatgpt.com "Deploying Apps with the Mule Maven Plugin"

[3]: https://www.jenkins.io/doc/pipeline/steps/credentials-binding/?utm_source=chatgpt.com "Credentials Binding Plugin"
