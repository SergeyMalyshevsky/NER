# NER

NER is a service for recognize entities from russian text. This service can used different libraries for information extraction.
List of Named-entity recognition libraries or services you can see on [this page](https://nlpub.ru/%D0%98%D0%B7%D0%B2%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5_%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85_%D1%81%D1%83%D1%89%D0%BD%D0%BE%D1%81%D1%82%D0%B5%D0%B9).
Most of them have commercial license. But there are some libraries which free for use.
Our NER service use other libraries to recognize named entities and union them. After that it removes duplicated elements and validates values by dictionaries.
For example, we can use dictionaries of names and sirnames, FIAS base for checking location and address information and etc.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python 3.x must be installed on your computer. If you haven't it, you can download Python 3 from [official site](https://www.python.org/downloads/).

### Installing

Clone project using Git:

```
git clone https://github.com/SergeyMalyshevsky/ner.git
```

Go to created directory:

```
cd ner
```

Install necessary libraries using pip:

```
pip install -r requirements.txt
```

Run local web server:

```
python app.py
```

Use Postman or another software to send POST request to address http://127.0.0.1:5000/ner/api/v0.1/
Body of request have to contain two elements: 
- text - source text in which we will search entities
- param - array of entity types which we will find. It can use following values: "name", "date", "location", "address", "money".
If we set value "all", service return all types of entities.

## Example

### Request

	{
	"text":"16 июля 2018 года вице-президент «Монако» Вадим Васильев сообщил о желании заключить с Александром Головиным пятилетний контракт[31]. 27 июля было официально объявлено о его переходе в «Монако». Срок контракта рассчитан на 5 лет[32]. Сумма трансфера составила 30 миллионов евро, что стало рекордно дорогим для российских футболистов[33]. Также трансфер Головина оказался третьим по цене среди игроков, которых российские клубы когда-либо продавали за границу. Его зарплата составит около 2 миллионов евро в год[34]. Ранее на него претендовал «Наполи», когда главным тренером команды был Маурицио Сарри. После его перехода в «Челси» лондонский клуб также пытался приобрести Головина. В число претендентов на него также входил «Ювентус»[35]. 5 августа провёл первую тренировку в составе «Монако». 8 августа получил первую травму в составе «Монако», не успев дебютировать в стартовом составе[36]. 20 августа был представлен в качестве игрока «красно-белых».",
	"param":["name", "date", "location", "address", "money"]
	}

### Response

	{
    "entities": {
        "address": [],
        "date": [
            {
                "current_era": true,
                "day": 16,
                "month": 7,
                "year": 2018
            },
            {
                "current_era": true,
                "day": 27,
                "month": 7
            },
            {
                "current_era": true,
                "day": 5,
                "month": 8
            },
            {
                "current_era": true,
                "day": 8,
                "month": 8
            },
            {
                "current_era": true,
                "day": 20,
                "month": 8
            }
        ],
        "location": [
            "монако"
        ],
        "money": [
            {
                "amount": 30000000,
                "currency": "EUR"
            },
            {
                "amount": 2000000,
                "currency": "EUR"
            }
        ],
        "name": [
            {
                "first": "александр",
                "last": "головин",
                "middle": ""
            },
            {
                "first": "вадим",
                "last": "васильев",
                "middle": ""
            },
            {
                "first": "маурицио",
                "last": "сарри",
                "middle": ""
            },
            {
                "first": "жан",
                "last": "",
                "middle": ""
            },
            {
                "first": "виллем",
                "last": "",
                "middle": ""
            },
            {
                "first": "",
                "last": "головин",
                "middle": ""
            },
            {
                "first": "эда",
                "last": "",
                "middle": ""
            }
        ]
    },
    "text": "16 июля 2018 года вице-президент «Монако» Вадим Васильев сообщил о желании заключить с Александром Головиным пятилетний контракт[31]. 27 июля было официально объявлено о его переходе в «Монако». Срок контракта рассчитан на 5 лет[32]. Сумма трансфера составила 30 миллионов евро, что стало рекордно дорогим для российских футболистов[33]. Также трансфер Головина оказался третьим по цене среди игроков, которых российские клубы когда-либо продавали за границу. Его зарплата составит около 2 миллионов евро в год[34]. Ранее на него претендовал «Наполи», когда главным тренером команды был Маурицио Сарри. После его перехода в «Челси» лондонский клуб также пытался приобрести Головина. В число претендентов на него также входил «Ювентус»[35]. 5 августа провёл первую тренировку в составе «Монако». 8 августа получил первую травму в составе «Монако», не успев дебютировать в стартовом составе[36]. 20 августа был представлен в качестве игрока «красно-белых». С Головиным также были представлены два других новичка клуба — полузащитник Жан-Эд Ахолу и форвард Виллем Жеббель."
	}


## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Pip](https://pip.pypa.io/en/stable/user_guide/) - Package Management
* [IPython](https://ipython.org/) - Command shell for interactive computing
* [Natasha](https://natasha.readthedocs.io/ru/latest/) - Library which recognize entities from text


## Author

* **Sergey Malyshevsky** - [NER](https://github.com/SergeyMalyshevsky)

See also the list of [contributors](https://github.com/ner/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
