# CARTESIAN ENIGMA

Welcome to the Internet Police. We're fighting criminals from the dark web. Our worst ennemies are black hat hackers doing criminal activities. They have a secret messaging system that we were not able to breach. After a complicated operation in real life we managed to retrieve the software they use to encode their messages, but we don't have the decoder. For now we're only storing the intercepted messages and it's critical for us to read their content!

## Encoding

Our cost effective experts have studied the script and have some understanding on how the message is encoded:

1. The message is stripped from all spacing characters
2. The message is splitted in slices of two characters
3. The slices are separated in two sets
4. The encoded message is the cartesian product of the two sets

Example:

```
MESSAGE         : "A BCD1 234"
STEP1           : "ABCD1234"
STEP2           : "AB CD 12 34"
STEP3           : {AB,CD} {12,34}
ENCODED MESSAGE : "AB12 AB34 CD12 CD34"
```

Here is how to use the encoder to encode that message:

```bash
agent@sidekickcomputer:~/boring_work/git/cartesian_enigma$ ./cartesian_enigma.sh A BCD1 234
AB12 AB34 CD12 CD34 
```

## Decoding

We need **YOU** to write the decoder so we can counter their evil plans! We're giving you the encoder. Don't damage it, it's our only copy.

Here is the last message we received:

```
Plca Plti Plti Plsr Plea Plll Plya Plnn Ploy Plin Plg. PlIp Plre Plfe Plrd Plog Pls eaca eati eati easr eaea eall eaya eann eaoy eain eag. eaIp eare eafe eard eaog eas seca seti seti sesr seea sell seya senn seoy sein seg. seIp sere sefe serd seog ses stca stti stti stsr stea stll stya stnn stoy stin stg. stIp stre stfe strd stog sts opca opti opti opsr opea opll opya opnn opoy opin opg. opIp opre opfe oprd opog ops seca seti seti sesr seea sell seya senn seoy sein seg. seIp sere sefe serd seog ses ndca ndti ndti ndsr ndea ndll ndya ndnn ndoy ndin ndg. ndIp ndre ndfe ndrd ndog nds inca inti inti insr inea inll inya innn inoy inin ing. inIp inre infe inrd inog ins gmca gmti gmti gmsr gmea gmll gmya gmnn gmoy gmin gmg. gmIp gmre gmfe gmrd gmog gms epca epti epti epsr epea epll epya epnn epoy epin epg. epIp epre epfe eprd epog eps icca icti icti icsr icea icll icya icnn icoy icin icg. icIp icre icfe icrd icog ics tuca tuti tuti tusr tuea tull tuya tunn tuoy tuin tug. tuIp ture tufe turd tuog tus reca reti reti resr reea rell reya renn reoy rein reg. reIp rere refe rerd reog res soca soti soti sosr soea soll soya sonn sooy soin sog. soIp sore sofe sord soog sos fyca fyti fyti fysr fyea fyll fyya fynn fyoy fyin fyg. fyIp fyre fyfe fyrd fyog fys ouca outi outi ousr ouea oull ouya ounn ouoy ouin oug. ouIp oure oufe ourd ouog ous rca rti rti rsr rea rll rya rnn roy rin rg. rIp rre rfe rrd rog rs
```

We're worried that it might be the order for something terrible! We need you to realize that decoder quickly to help us save the world! Also, please don't charge us too much as our budget is limited this year.
