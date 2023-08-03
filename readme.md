# Azure Functions Instructions

### Install Anaconda from this website for both m1 and intel processors
```
https://www.anaconda.com/
```

### Install version 3.9.2/3.10 
```shell
conda create -n Py310 python=3.10
conda activate Py310

brew install azure-cli
```

### install azure function core tools
```shell
brew tap azure/functions
brew install azure-functions-core-tools@4
# if upgrading on a machine that has 2.x or 3.x installed:
brew link --overwrite azure-functions-core-tools@4
```

### Modify these variables as per your choice
```shell
export RESOURCE_GROUP_NAME=OpenAiResourceGroup
export AZURE_LOCATION=eastus
export STORAGE_NAME=uopdsstorage
export AZURE_FUNCTIONS_APP_NAME=uop-app-name-1
```


### create folder of your choice in terminal

```shell
mkdir -p ~/Projects/azure
```

#### if you get error with venv install this and repeat above step from terminal
```shell
sudo apt-get install python3-venv
```

### activate the virtual envfrom terminal
```shell
source .venv/bin/activate
```

### create the azure functions app project folder from terminal can be any name
```shell
func init uop_ds_app --python
```

### create function inside the app. from terminal
```shell
func new --name OpenApiHttp --template "HTTP trigger" --authlevel "anonymous"
```

### to run the function locally from terminal
```shell
func start
```

### login to Azure from terminal
```shell
az login
```

### create azure resource group its a logical partition for resources
```shell
az group create --name $RESOURCE_GROUP_NAME --location $AZURE_LOCATION
```

### create storage account
```shell
az storage account create --name $STORAGE_NAME --location $AZURE_LOCATION --resource-group $RESOURCE_GROUP_NAME --sku Standard_LRS
```

### create  az function app
```shell
az functionapp create --resource-group $RESOURCE_GROUP_NAME --consumption-plan-location $AZURE_LOCATION --runtime python --runtime-version 3.10 --functions-version 4 --name $STORAGE_NAME --os-type linux --storage-account $STORAGE_NAME
```

### deploy the app
```shell
func azure functionapp publish $AZURE_FUNCTIONS_APP_NAME
```
