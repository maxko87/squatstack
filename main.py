import requests, time

WORDS = ["time","year","people","way","day","man","thing","woman","life","child","world","school","state","family","student","group","country","problem","hand","part","place","case","week","company","system","program","question","work","government","number","night","point","home","water","room","mother","area","money","story","fact","month","lot","right","study","book","eye","job","word","business","issue","side","kind","head","house","service","friend","father","power","hour","game","line","end","member","law","car","city","community","name","president","team","minute","idea","kid","body","information","back","parent","face","others","level","office","door","health","person","art","war","history","party","result","change","morning","reason","research","girl","guy","moment","air","teacher","force","education"]
WORDS_PLURAL = ["times","years","peoples","ways","days","men","things","women","lifes","childs","worlds","schools","states","families","students","groups","countries","problems","hands","parts","places","cases","weeks","companies","systems","programs","questions","works","governments","numbers","nights","points","homes","waters","rooms","mothers","areas","moneys","stories","facts","months","lots","rights","studys","books","eyes","jobs","words","businesss","issues","sides","kinds","heads","houses","services","friends","fathers","powers","hours","games","lines","ends","members","laws","cars","cities","communities","names","presidents","teams","minutes","ideas","kids","bodies","informations","backs","parents","faces","other","levels","offices","doors","healths","persons","arts","wars","histories","parties","results","changes","mornings","reasons","researches","girls","guys","moments","airs","teachers","forces","educations"]
MALE_NAMES = ["james","john","robert","michael","william","david","richard","charles","joseph","thomas","christopher","daniel","paul","mark","donald","george","kenneth","steven","edward","brian","ronald","anthony","kevin","jason","matthew","gary","timothy","jose","larry","jeffrey","frank","scott","eric","stephen","andrew","raymond","gregory","joshua","jerry","dennis","walter","patrick","peter","harold","douglas","henry","carl","arthur","ryan","roger","joe","juan","jack","albert","jonathan","justin","terry","gerald","keith","samuel","willie","ralph","lawrence","nicholas","roy","benjamin","bruce","brandon","adam","harry","fred","wayne","billy","steve","louis","jeremy","aaron","randy","howard","eugene","carlos","russell","bobby","victor","martin","ernest","phillip","todd","jesse","craig","alan","shawn","clarence","sean","philip","chris","johnny","earl","jimmy","antonio"]
FEMALE_NAMES = ["olivia","emma","ava","sophia","isabella","charlotte","amelia","mia","harper","evelyn","abigail","emily","ella","elizabeth","camila","luna","sofia","avery","mila","aria","scarlett","penelope","layla","chloe","victoria","madison","eleanor","grace","nora","riley","zoey","hannah","hazel","lily","ellie","violet","lillian","zoe","stella","aurora","natalie","emilia","beverly","leah","aubrey","willow","addison","lucy","audrey","bella","nova","brooklyn","paisley","savannah","claire","skylar","isla","genesis","naomi","elena","caroline","eliana","anna","maya","valentina","ruby","kennedy","ivy","ariana","aaliyah","cora","madelyn","alice","kinsley","hailey","gabriella","allison","gianna","serenity","samantha","sarah","autumn","quinn","eva","piper","sophie","sadie","delilah","josephine","nevaeh","adeline","arya","emery","lydia","clara","vivian","madeline","peyton","julia","rylee"]

SUBSTACK_URL = "https://{}.substack.com"
SUBSTACK_NOT_TAKEN_URL = "https://substack.com/discover/{}"

def check_substack_available(prefix):
    url = SUBSTACK_URL.format(prefix)
    not_taken_url = SUBSTACK_NOT_TAKEN_URL.format(prefix)

    r = requests.get(url, allow_redirects=False)
    time.sleep(.5)

    redirect_location = r.headers.get('location')

    if redirect_location == not_taken_url:
        print("!! {} is available: {}".format(prefix, url))
        return True
    else:
        print("{} is taken".format(url))
        return False

if __name__ == '__main__':
    for prefix in WORDS_PLURAL: # or MALE_NAMES or FEMALE_NAMES
        check_substack_available(prefix)
