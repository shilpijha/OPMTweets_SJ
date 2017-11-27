# This Python file uses the following encoding: utf-8
import re 
from nltk.corpus import stopwords

# Hashtags
hash_regex = re.compile(r"#(\w+)")
def hash_repl(match):
    return '__HASH_'+match.group(1).upper()

rt_regex = re.compile(r"RT")

# Handels
hndl_regex = re.compile(r"@(\w+)")
def hndl_repl(match):
    return '__HNDL'#_'+match.group(1).upper()

# Ampersands
amp_regex = re.compile(r"&(\w+)")
def amp_repl(match):
    return '__AMP'#_'+match.group(1).upper()

#digits
dig_regex=re.compile(r"(\d)")

#singleLetter
sig_let=re.compile(r"(?i)\b[a-z]\b") #catch only single letters case insensitive

#doubleLetter
double_let=re.compile(r"(?i)\b[a-z][a-z]\b") #catch only double letters case insensitive

# URLs
url_regex = re.compile(r"(http|https|ftp)://[a-zA-Z0-9\./]+")

# Spliting by word boundaries
word_bound_regex = re.compile(r"\W+")

# Repeating words like hurrrryyyyyy
rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE);
def rpt_repl(match):
    return match.group(1)+match.group(1)

# Emoticons
emoticons = \
    [	('__EMOT_SMILEY',	[':-)', ':)', '(:', '(-:', ] )	,\
        ('__EMOT_LAUGH',		[':-D', ':D', 'X-D', 'XD', 'xD', ] )	,\
        ('__EMOT_LOVE',		['<3', ':\*', ] )	,\
        ('__EMOT_WINK',		[';-)', ';)', ';-D', ';D', '(;', '(-;', ] )	,\
        ('__EMOT_FROWN',		[':-(', ':(', '(:', '(-:', ] )	,\
        ('__EMOT_CRY',		[':,(', ':\'(', ':"(', ':(('] )	,\
    ]

# Punctuations
punctuations = \
    [	#('',		['.', ] )	,\
        #('',		[',', ] )	,\
        #('',		['\'', '\"', ] )	,\
        ('__PUNC_EXCL',		['!', '¡', ] )	,\
        ('__PUNC_QUES',		['?', '¿', ] )	,\
        ('__PUNC_ELLP',		['...', '…', ] )	,\
        #FIXME : MORE? http://en.wikipedia.org/wiki/Punctuation
    ]

#Printing functions for info
def print_config(cfg):
    for (x, arr) in cfg:
        print (x, '\t'),
        for a in arr:
            print (a, '\t'),
        print ('')

def print_emoticons():
    print_config(emoticons)

def print_punctuations():
    print_config(punctuations)

#For emoticon regexes
def escape_paren(arr):
    return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]

def regex_union(arr):
    return '(' + '|'.join( arr ) + ')'

emoticons_regex = [ (repl, re.compile(regex_union(escape_paren(regx))) ) \
                    for (repl, regx) in emoticons ]

#For punctuation replacement
def punctuations_repl(match):
    text = match.group(0)
    repl = []
    for (key, parr) in punctuations :
        for punc in parr :
            if punc in text:
                repl.append(key)
    if( len(repl)>0 ) :
        return ' '+' '.join(repl)+' '
    else :
        return ' '

def processHashtags( 	text, subject='', query=[]):
    return re.sub( hash_regex, hash_repl, text )

def processHandles( 	text, subject='', query=[]):
    return re.sub( hndl_regex, hndl_repl, text )

def processUrls( 		text, subject='', query=[]):
    return re.sub( url_regex, ' __URL ', text )

def processEmoticons( 	text, subject='', query=[]):
    for (repl, regx) in emoticons_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    return text

def processPunctuations( text, subject='', query=[]):
    return re.sub( word_bound_regex , punctuations_repl, text )

def processRepeatings( 	text, subject='', query=[]):
    return re.sub( rpt_regex, rpt_repl, text )

def processQueryTerm( 	text, subject='', query=[]):
    query_regex = "|".join([ re.escape(q) for q in query])
    return re.sub( query_regex, '__QUER', text, flags=re.IGNORECASE )

def countHandles(text):
    return len( re.findall( hndl_regex, text) )
def countHashtags(text):
    return len( re.findall( hash_regex, text) )
def countUrls(text):
    return len( re.findall( url_regex, text) )
def countEmoticons(text):
    count = 0
    for (repl, regx) in emoticons_regex :
        count += len( re.findall( regx, text) )
    return count

#FIXME: preprocessing.preprocess() will need to move.
#FIXME: use process functions inside
def processAll( text, subject='', query=[]):


    cachedStopWords = stopwords.words("english") #not sufficient list of words ... use manual list

    if(len(query)>0):
        query_regex = "|".join([ re.escape(q) for q in query])
        text = re.sub( query_regex, '__QUER', text, flags=re.IGNORECASE )

    #text = re.sub( hash_regex,processHashtags(text), text )
    text = re.sub(hash_regex, '', text) #remove #
    text = re.sub(hndl_regex, '', text ) #remove @
    text = re.sub(amp_regex, '', text)  # remove &
    text = re.sub(url_regex, '', text ) #remove urls
    text = re.sub(rt_regex, '', text )  #remove RT word
    text = re.sub(dig_regex, '', text ) #remove digits
    text = re.sub(sig_let, '', text ) #remove single letters
    text = re.sub(double_let, '', text)  # remove double letters

    manual_stopwords_list = "a,s,able,about,above,according,accordingly,across,actually,after,afterwards,again,against,ain,t,all,allow,allows,almost,alone,along,already,also,although,always,am,among,amongst,an,and,another,any,anybody,anyhow,anyone,anything,anyway,anyways,anywhere,apart,appear,appreciate,appropriate,are,aren,t,around,as,aside,ask,asking,associated,at,available,away,awfully,be,became,because,become,becomes,becoming,been,before,beforehand,behind,being,believe,below,beside,besides,best,better,between,beyond,both,brief,but,by,c,mon,c,s,came,can,can,t,cannot,cant,cause,causes,certain,certainly,changes,clearly,co,com,come,comes,concerning,consequently,consider,considering,contain,containing,contains,corresponding,could,couldn,t,course,currently,definitely,described,despite,did,didn,t,different,do,does,doesn,t,doing,don,t,done,down,downwards,during,each,edu,eg,eight,either,else,elsewhere,enough,entirely,especially,et,etc,even,ever,every,everybody,everyone,everything,everywhere,ex,exactly,example,except,far,few,fifth,first,five,followed,following,follows,for,former,formerly,forth,four,from,further,furthermore,get,gets,getting,given,gives,go,goes,going,gone,got,gotten,greetings,had,hadn,t,happens,hardly,has,hasn,t,have,haven,t,having,he,he,s,hello,help,hence,her,here,here,s,hereafter,hereby,herein,hereupon,hers,herself,hi,him,himself,his,hither,hopefully,how,howbeit,however,i,d,i,ll,i,m,i,ve,ie,if,ignored,immediate,in,inasmuch,inc,indeed,indicate,indicated,indicates,inner,insofar,instead,into,inward,is,isn,t,it,it,d,it,ll,it,s,its,itself,just,keep,keeps,kept,know,knows,known,last,lately,later,latter,latterly,least,less,lest,let,let,s,like,liked,likely,little,look,looking,looks,ltd,mainly,many,may,maybe,me,mean,meanwhile,merely,might,more,moreover,most,mostly,much,must,my,myself,name,namely,nd,near,nearly,necessary,need,needs,neither,never,nevertheless,new,next,nine,no,nobody,non,none,noone,nor,normally,not,nothing,novel,now,nowhere,obviously,of,off,often,oh,ok,okay,old,on,once,one,ones,only,onto,or,other,others,otherwise,ought,our,ours,ourselves,out,outside,over,overall,own,particular,particularly,per,perhaps,placed,please,plus,possible,presumably,probably,provides,que,quite,qv,rather,rd,re,really,reasonably,regarding,regardless,regards,relatively,respectively,right,said,same,saw,say,saying,says,second,secondly,see,seeing,seem,seemed,seeming,seems,seen,self,selves,sensible,sent,serious,seriously,seven,several,shall,she,should,shouldn,t,since,six,so,some,somebody,somehow,someone,something,sometime,sometimes,somewhat,somewhere,soon,sorry,specified,specify,specifying,still,sub,such,sup,sure,t,s,take,taken,tell,tends,th,than,thank,thanks,thanx,that,that,s,thats,the,their,theirs,them,themselves,then,thence,there,there,s,thereafter,thereby,therefore,therein,theres,thereupon,these,they,they,d,they,ll,they,re,they,ve,think,third,this,thorough,thoroughly,those,though,three,through,throughout,thru,thus,to,together,too,took,toward,towards,tried,tries,truly,try,trying,twice,two,un,under,unfortunately,unless,unlikely,until,unto,up,upon,us,use,used,useful,uses,using,usually,value,various,very,via,viz,vs,want,wants,was,wasn,t,way,we,we,d,we,ll,we,re,we,ve,welcome,well,went,were,weren,t,what,what,s,whatever,when,whence,whenever,where,where,s,whereafter,whereas,whereby,wherein,whereupon,wherever,whether,which,while,whither,who,who,s,whoever,whole,whom,whose,why,will,willing,wish,with,within,without,won,t,wonder,would,would,wouldn,t,yes,yet,you,you,d,you,ll,you,re,you,ve,your,yours,yourself,yourselves,zero".split(
        ',')
    pattern = re.compile(r'(?i)\b(' + r'|'.join(manual_stopwords_list) + r')\b\s*')
    text = pattern.sub('', text)  # remove all stopwords from tweets

    for (repl, regx) in emoticons_regex :
        text = re.sub(regx, ' '+repl+' ', text)

    text = text.replace('\'','')
    text = text.replace('_', '') #remove underscores
    # FIXME: Jugad

    text = re.sub( word_bound_regex , ' ', text )
    text = re.sub( rpt_regex, rpt_repl, text )
    text=' '.join([word for word in text.split() if word.lower() not in cachedStopWords])

    return text


