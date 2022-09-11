def timetable(weekday):
    tt = {
        "Monday": [
            [
                "7:45",
                "9:05",
                ["Physics - Lab", "Biology - 12", "Accounting - 20", "History - 26"],
            ],
            [
                "9:30",
                "10:10",
                ["English"]
            ],
            [
                "10:10",
                "10:50",
                ["Religious knowledge - 20, 12", "Religious studies - 26, G35"]
            ],
            [
                "11:05",
                "12:25",
                ["Modern Greek - 20", "GFL - 26, 24"]
            ],
            [
                "12:40",
                "14:00",
                ["ART - G33", "ICT - Lab 1", "Chemistry - 12", "Economics - 26"]
            ],
            [
                "14:25",
                "15:45",
                ["Biology 2 - 12"]
            ]
        ],
        'Tuesday':[
            [
                '7:45',
                '9:05',
                ["Physics - 20", "Biology - 12", "Accounting - 26", "History - G27"]
            ],
            [
                "9:30",
                "10:50",
                ["Art - G33", "ICT - Lab 1", "Chemistry - Lab", "Economics - 12"]
            ],
            [
                "11:05",
                "12:25",
                ["Modern Greek - 20", "GFL - 26, G35"]
            ],
            [
                "12:40",
                "14:00",
                ["Math 4 - 20, 12", "Business studies - 16", "Politics - 26"]
            ]
        ],
        "Wednesday":[
            [
                "7:45",
                "9:05",
                ["English"]
            ],
            [
                "9:30",
                "9:40",
                ["Form Period"]
            ],
            [
                "9:40",
                "11:00",
                ["Math 4 - 20, 12", "Math 2 - 26, 19"]
            ],
            [
                "11:15",
                "12:35",
                ["Art - G33", "ICT - Lab 1", "Chemistery - 12", "Economics - 20"]
            ],
            [
                "12:45",
                "14:05",
                ["Physics - 12", "Biology - Lab", "Accounting - 20", "History - 26"]
            ]
        ],
        "Thursday":[
            [
                "7:45",
                "9:05",
                ["English"]
            ],
            [
                "9:30",
                "10:10",
                ["Modern Greek - 20", "GFL - 26, G34"]
            ],
            [
                "10:10",
                "10:50",
                ["Greek History - 20", "GFL - 26, G34"]
            ],
            [
                "11:05",
                "12:25",
                ["Math 4 - 20, 12", "Business studies - 16", "Politics - 26"]
            ],
            [
                "12:40",
                "14:00",
                ["Art - G33", "ICT - Lab 1", "Chemistry - Lab", "Economics - 12"]
            ],
            [
                "14:25",
                "15:45",
                ["Biology 2 - 12"]
            ]
        ],
        "Friday":[
            [
                "7:45",
                "9:05",
                ["Math 4 - 20, 12", "Math 2 - 26, 24"]
            ],
            [
                "9:30",
                "10:50",
                ["Physical Education", "Business studies - 16", "Biology 2 - 17A"]
            ],
            [
                "11:05",
                "12:25",
                ["ICT Core - Lab 1, Lab 3", "Biology 2 - Lab", "Politics - 12"]
            ],
            [
                "12:40",
                "14:00",
                ["Physics - 12", "Biology - 20", "Accounting - 26", "History - 14"]
            ]
        ]
    }
    return tt[weekday]