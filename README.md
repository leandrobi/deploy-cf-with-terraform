# Test Deploy - Terraform for GCF
_pt-br:_

Este repositório é um teste para realização de um deploy para o serviço do Google Cloud Function utilizando Terraform.

## Tenha em seu computador...

1. vsCode (https://code.visualstudio.com/download)
2. Terraform (https://developer.hashicorp.com/terraform/install)
    > Após download, salve o arquivo .exe dentro de c:\Program files\Terraform e adicione a pasta na variável path do sistema. Em seguida, teste o terraform no console utilizando o comando terraform --version
3. Python (https://www.python.org/downloads/)
    > No começo da instalação, ative a opção para setar a variável de ambiente
4. Git (https://git-scm.com/downloads)
5. GCloud Cli (https://cloud.google.com/sdk/docs/install?hl=pt-br)
    > Após instalação, execute o comando gloud init para iniciar a autenticação

## No GCP...

1. Um novo projeto de teste.
2. Ative as APIs Cloud Functions, Cloud Run, Cloud Build, Artifact Registry, and Cloud Storage.
    https://console.cloud.google.com/flows/enableapi?apiid=cloudbuild.googleapis.com%2Crun.googleapis.com%2Cartifactregistry.googleapis.com%2Ccloudfunctions.googleapis.com%2Cstorage.googleapis.com&%3Bredirect=https%3A%2F%2Fcloud.google.com%2Ffunctions%2Fdocs%2Ftutorials%2Fterraform&hl=pt-br&_ga=2.145621876.1144589206.1708107338-54807114.1692367092&_gac=1.148005445.1706744182.CjwKCAiA_OetBhAtEiwAPTeQZ1Ca3Vvw9xohy0CRv8OFW5-TFXqPcPyw_wyU6ulbFSRjbu9F87fiehoCky4QAvD_BwE
3. Uma conta de serviço do IAM com chave json e liberação de Editor para manipular storage e cloud function

## No visual code...
1. Clone este repositório e crie uma pasta chamada .keys na raiz para deixar o arquivo json da chave gcp
2. Na raiz do projeto, abra o vscode e aperte ctrl + ' para abrir o terminal
3. Edite as linhas abaixo do arquivo main.tf

    * O local da chave json e o project_id do projeto:
        ```
        provider "google" {
        credentials = file(".keys/testtodeploycf-f5ee86da52dc.json")
        project = "testtodeploycf"
        }
        ```
    * O nome da função precisa ser única na região, por isso altere o nome:
        ```
        resource "google_cloudfunctions2_function" "default" {
        name        = "function-v2-test-with-terraform"
        ...}
        ```

    * Analise o main.tf para editar outros pontos que achar pertinente...

4. No terminal dentro do vscode, digite _terraform init_ e dê enter
5. Em seguida digite _terraform apply_ e dê enter
    > Se tudo deu certo, após a finalização deste comando, você já terá sua função no GCF.
    O scrip do terraform (main.tf) esta configurado para subir a função utilizando o storage como fonte da função, ou seja, é por isso que a chave json da conta de serviço precisa ter permissão pra usar o storage.
6. Para encerrar os serviços criados, basta executar _terraform destroy_ em seu terminal do vscode

## Após implantação e antes do destroy...
1. Capture a URL da sua função no console trocando o nome dela:
    ``` 
    gcloud functions describe function-v2-test-with-terraform --gen2 --region=southamerica-east1 --format="value(serviceConfig.uri)
    ```

2. Execute a chamada http:
    ```
    curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" YOUR_FUNCTION_URL
    ```

