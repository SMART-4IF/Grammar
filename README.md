# Grammar
This model allows you to transform a sequence of words into a sentence grammatically correct.
Indeed, in sign language, we will for example sign "yesterday cinema go me" to sign "Yesterday I went to the cinema". This model is only for french language.

# How it works 
This model was developped with the TTT method. 
When you send it 4 words or less, it will find the verb, if there is a time marker and the subject. After that it's gonna conjugate the verb according to the person and the tense found prevously. Then, it will find the complement. 

# Installation
You have to install the module that conjugate the verb with the command ````pip install verbecc```

