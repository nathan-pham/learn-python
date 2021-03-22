# No exercises; Twitter & Google APIs require developer authentication

import json

data = """{
	"name": "Nathan Pham",
	"phone": {
		"type": "intl",
		"number": "+1 916 802 0725"
	},
	"email": {
		"hide": true
	}
}"""

serialized = json.loads(data)
print(serialized["email"]["hide"])