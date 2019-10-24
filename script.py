WELCOME_PHRASES = [
  "Welche fragen hast du über die Bulme?",
  "Wie kann ich dir behilflich sein?",
  "Hast du Fragen über unsere Schule?",
  "Stelle mir eine Frage über die Bulme?"
]
DEFAULT_ANSWERS = [
  "Ich muss darüber nachdenken.",
  "Bitte formuliere deine Frage neu.",
  "this sounds interesting.",
  "let me think about it.",
  "please tell me more.",
  "and...?"
  ]

GOODBYE_PHRASES = [
  "Ich wünsche dir noch einen schönen Tag!",
  "Tschüss.",
  "Auf Wiedersehen!",
  "Auf Wiedersehen, ich hoffe ich konnte dir helfen!"
]


# this list contains all the rules to transform user input into answers.
# each rule is a list with two elements:
# – the first element is a search-pattern, given as a string or a regular expression
# – the second element is a list of related answer-patterns
#
# [search_pattern,
#  [answer_pattern,
#   answer_pattern,
#   answer_pattern,
#    ...]
# ]


rules = [

  # keywords without personal pronoun

  [r"bitch|fick dich|arschloch|hure",
   ["Bitte benutze Wörter wie '%MATCH' nicht!",
    "Wieso bist du so wütend?"]
   ],

  [r"elektronik",
   ["Man lern programmieren, Bluetooth verstehen, Geräte entwickeln von Audioverstärker bis Zufallsgenerator.",
   ]
   ],
  
  [r"zweig|zweige|ausbildungszweige",
   ["Die Bulme bietet: Maschinenbau, Wirtschaftsingeneurwesen, Elektronik & technische Informatik, Elektrotechnik"]
   ],
  
  [r"schwerpunkte|wahlpflichtfächer",
   ["Die Elektoronik bietet Wahlpflichtfächer wie: Biomedizin, Softwareentwicklung, Netzwerktechnik, Audioelektronik"]
   ],
  
  [r"schwerpunkte|wahlpflichtfächer | elektronik",
   ["Die Elektoronik bietet Wahlpflichtfächer wie: Biomedizin, Softwareentwicklung, Netzwerktechnik, Audioelektronik"]
   ],

  ["mädchen",
   ["Leider sind Maschinenbauerinnen oder Elektrotechnikerinnen noch immer die Ausnahme in der Welt der Technik. Erfolge gibt es aber zu verbuchen, denn in den HTLs hat sich der Mädchenanteil in den letzten 25 Jahren um fast 300 Prozent gesteigert. Unsere Schule bietet den Mädchen den passenden Einstieg in die Welt der Technik und haltet ihnen die Türen offen zu interessierten Betrieben und Weiterbildungsangeboten nach der Reife- und Diplomprüfung. Denn die Industrie sucht händeringend nach technischen Fachkräften, immer stärker auch nach weiblichen Fachkräften.Eine Mädchenbeauftragte vernetzt die Tagschülerinnen, es gibt immer wieder gemeinsame Aktivitäten. Wir erkennen das Potential unserer Schülerinnen und versuchen sie auf ihrem Weg zu unterstützen"]
   ],

  [r"perhaps|possibly|maybe|probably",
   ["you aren't very confident about that.",
    "this sounds quite doubtful."]
   ],

  ["dream",
   ["tell me about your dreams.",
    "do you dream often?"]
   ],

  ["friend",
   ["do you have many friends?",
    "what do your friends mean to you?"]
   ],

  [r"alike|similar|equal|same",
   ["in what way?",
    "how?"]
   ],

  [r"rich|wealthy|poor|broke|bankrupt|money|debt",
   ["do you have financial problems?",
    "how important is money in your life?"]
   ],

  [r"loss|lost",
   ["tell me more about this loss",
    "it can be hard to loose %POST_MATCH"]
   ],

  [r"computer|chatbot|machine|programm|code",
   ["are you afraid of %MATCHs?",
    "is it a problem for you that i am a %MATCH?"]
   ],

  [r"thank you|thanks",
   ["you're welcome.",
    "no problem."]
   ],

  [r"mother|father|sister|brother|daughter|\bson\b|daughter",
   ["please tell me more about your family.",
    "how is your relationship to your %MATCH?",
    "do you love your %MATCH?",
    "what kind of influence does your %MATCH have on you?"]
   ],

  [r"sure|yes|yeah|exactly",
   ["actually i'm not that sure.",
    "you seem to be quite certain about that.",
    "ok. please go on.",
    "how can you be so sure?"]
   ],

  [r"^(ok|okay|o\.k\.|i agree|agreed)(\.|$)",
   ["great.",
    "so we agree on this point."]
   ],
  
# i and verb "are"

   [r"i (am|feel)(?! not).*(sad|depressive|depressed|unhappy|sick)",
    ["sorry to hear that you are feeling bad.",
     "where do these bad feelings come from?",
     "what could make you feel better?",
     "how can i support you to solve your problems?"]
    ],

  [r"i am(?! not) afraid of",
   ["what would be the worst thing that could happen?",
    "please tell me more about those fears.",
    "why do you fear %POST_MATCH?",
    "what else do you fear?"]
   ],
  
  [r"i am",
   ["why do you say that you are %POST_MATCH?",
    "since when do you have the idea that you are %POST_MATCH?",
    "do other people agree that you are %POST_MATCH?",
    "who said that?"]
   ],
  
### i + other verbs

  [r"i have",
   ["who said that you have %POST_MATCH?",
    "why do you have %POST_MATCH?"]
   ],

  [r"i feel|i am feeling",
   ["please tell me more about these feelings.",
    "do you often feel %POST_MATCH?",
    "do you like to feel %POST_MATCH?",
    "what makes you feel %POST_MATCH?"]
    ],
  
  [r"i want",
   ["why do you want %POST_MATCH?",
    "what if you never got %POST_MATCH?",
    "what would it mean to you if you got %POST_MATCH?",
    "sometimes i also want %POST_MATCH."]
    ],

  [r"i (do not|don't) want",
   ["have you ever tried %POST_MATCH?",
    "why don't you want %POST_MATCH?"]
   ],
  
  [r"i (do not|don't)",
   ["why are you so negative?",
    "you seem to be quite defensive."]
   ],

  [r"i (must|may) not",
   ["who said that you may not %POST_MATCH?",
    "you may not %POST_MATCH  or do you just not dare to?"]
   ],

  [r"i wish",
   ["what else would change if your wish came true?",
    "where does this desire come from?"]
   ],

  [r"i think",
   ["why do you think %POST_MATCH?",
    "what else do you think about this topic?"]
   ],

  ["i need",
   ["why do you need %POST_MATCH?",
    "do you sometimes get what you need?",
    "tell me more about your needs.",
    "sometimes we have to accept that we don't get what we need."]
   ],

  ["i believe",
   ["what makes you believe %POST_MATCH?",
    "why do you believe %POST_MATCH?"]
   ],

  [r"i hope",
   ["what would it mean to you if your hope would be fulfilled?",
    "what could you do to fullfil this wish?"]
   ],
  
  ["i love",
   ["what else do you love?",
    "what do you love most about %POST_MATCH?"]
   ],

### you + verb
  
  [r"you are(?! not)",
    ["why are you interested in whether or not i am %POST_MATCH?",
    "possibly i am %POST_MATCH, but what's your point?",
    "we should better focus on you.",
    "would you prefer if i were not %POST_MATCH?"]
  ],
  
### your + verb (questions)
  
  ["are you",
   ["why is it relevant if i am %POST_MATCH?",
    "we should better talk about you.",
    "do you wish me to be %POST_MATCH?",
    "would it help you to know that i am %POST_MATCH?"]
  ],
  
  ["can you",
   ["you want me to be able to %POST_MATCH?",
    "don't you believe that i can %POST_MATCH?",
    "perhaps you would like to be able to %POST_MATCH?",
    "i never tried."]
   ],

  ["did you",
   ["actually i'm not sure if i %POST_MATCH.",
    "Ich kann mich nicht erinnern.",
    "Wie ist das relevant für dich?",
    "Glaubst du das ich %POST_MATCH?"]
   ],

  ["do you",
   ["Ich kann dich das gleiche Fragen: %POST_MATCH?",
    "Willst du das ich %POST_MATCH?"]
   ],
  
### question- and exclamation mark

  [r"\?",
   ["Ist das eine wichtige Frage?",
    "Wieso fragst du?",
    "Ich weiss es nicht.",
    "Gute Frage.",
    "Gibt es etwas was du wircklich wissen willst?",
    "Was denkst du?"]
   ],
  
  [r"\!",
   ["why are you so exited?",
    "calm down, please."]
   ],
  
### reflect all if there is something to reflect 

  [r"\bi\b|\bmy\b|\bmine\b|\bme\b|\byou",
    ["%COMPLETE.",
    "i see, %COMPLETE."]
  ]
  
]
