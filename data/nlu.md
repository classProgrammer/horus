## intent:are_you_a_bot
- bist du ein bot
- bist du ein mensch
- hast du gefühle
- bist du eine maschiene
- bist du ein roboter
- kannst du fühlen
- bist du echt
- bot?
- roboter?
- mensch?

## intent:cando
- Was kannst du?
- Was kannst du
- Wie kannst du mir helfen
- was machst du
- welche aktionen kannst du ausführen

## intent:fetch_sickness_data
- [Hans Wurst](name), [12.05.1986](dob)
- Ich bin [Anna Nass](name) geboren am [07.09.1958](dob)
- [Luke Skywalker](name) [07.09.1958](dob)
- [Rainer Maria](name): [05.03.1999](dob)
- [Stefani Alexander](name) : [31.08.1993](dob)
- [Hans Solo](name) :[01.01.2000](dob)
- [Maria Müller](name), [22.04.1977](dob)
- [Yoda Starwars](name) [30.03.1997](dob)
- [Ozzy Osbourne](name) [24.06.1994](dob)
- [Hans Wurst](name) [27.04.1997](dob)
- [Alfred Johansson](name), [12.12.2012](dob)
- [Scarlett Johansson](name)
- [Natalie Portman](name)
- [Michael Jackson](name)
- [Sebastian Berg](name)
- Anna Fakename
- 28.02.1999
- Johan Aichberger

## intent:goodbye
- tschau
- Auf Wiedersehen
- tschüss
- tschüs
- bye
- ende
- servus
- servas
- Guten Tag
- bis bald

## intent:greet
- Hi
- Hey
- Hallo
- Sup
- Hallo Bot
- Kannst du mir helfen?
- Bist du da
- Ich brauche deine Hilfe
- Ich brauche Hilfe
- Hi bot
- Hey bot
- hi

## intent:holiday
- Ich brauche Urlaub
- urlaub
- Urlaub
- Ich will Urlaub beantragen
- Ich will Urlaub
- Ich benötige Uralaub
- Urlaubsantrag

## intent:sickness
- Ich bin krank
- Mir geht es nicht gut
- Ich fühle mich nicht besonders
- Mir ist furchtbar übel
- Ich bin krank
- Ich bin heute unpässlich
- Ich habe Kopfschmerzen
- Ich komme heute nicht
- Ich komme heute nicht zur Arbeit
- Heute bin ich nicht da
- Heute bin ich krank
- Ich kann heute nicht zur Arbeit gehen
- ich bin krank
- Hi, ich bin krank. kannst du mir helfen?
- krankmelden
- krank
- ich bin krank, kannst du mir helfen?

## intent:stop
- stop
- stopp
- beenden
- abbrechen
- aufhören
- ende
- abbruch

## intent:thanks
- danke
- danke
- thx
- THX
- K THX
- vielen dank
- super
- perfekt
- wunderbar
- danke, du warst ziemlich hilfreich

## regex:dob
- ^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$

## regex:name
- ^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$
