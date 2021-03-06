# localizator
Download and format your Drive sheet to iOS or Android localized file

## Google Drive API KEY
If you don't have already an API key ( and you certainly don't ) visit https://developers.google.com/drive/v3/web/quickstart/python
Follow the Step 1 and 2.
You now have to move the *client_secret.json file into the localizator folder*.


##Dependencies
Python3 is required. If you don't have python3, go on https://www.python.org/downloads/


You may need to install several packages too

```shell
pip3 install httplib2
pip3 install google-api-python-client
```

##Usage
```shell
python3 localizator.py --help
```

##Nice to Have

I recommend you to create a `localizator.sh` file containing your command line

Exemple :
```shell
#localizator.sh
python3 localizator/localyzator.py --id=MY_SHEET_ID --path=PATH_TO_RESSOURCE
```

Then in your `bash_profile` add the `Localize` alias as following :

```shell
echo "alias Localize='sh localizator.sh'" >> ~/.bash_profile
#update your settings
source ~/.bash_profile
```

Now, simply run `Localize` from your workspace!


##iOS components
### Localizator.swift

Use Localizator.swift to download your Localizable strings from a distant server. It allow you to change your strings files while your app is on the appstore.

####Download
```swift
Localizator.synchronize { (success) in
            //Do some stuff here, like dismissing loader
 }
```

####Usage
Now you simply have to use the `Localizator.localizedString` function to localize your text.

```
//Exemple of strings file
"Hello" = "Bonjour";
```

```swift
myLabel.text = Localizator.localizedString("Hello")
//OR
myLabel.text = ~"Hello"

//You can also do myLabel.text = l("Hello")
//myLabel.text will be "Bonjour"
```



###LocalizedComponents.swift

Localized components are groups of UIComponentns ( as UILabel, UIButton, UITextfield...) which have some additionnal (IBInspectable) attributes.

For example, in you xib/storybord file, you can set the `localizedText` from `LocalizedLabel`. At the runtime, the `localizedText` will be replace by his localized value using the `Localizator.localizedString` function



