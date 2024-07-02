//Node-Redで制御しています

obniz.display.clear();
nobniz.display.print('Start measurement');

var led1 = obniz.wired("LED", { anode: 0, cathode: 1 });
led1.on();

obniz.wait(2000);//2秒待機

var tempsens = obniz.wired("MCP9701", { gnd: 9, output: 10, vcc: 11 });
var temp = parseInt(await tempsens.getWait());

obniz.wait(2000);//2秒待機

obniz.display.clear();
obniz.display.print("Now Temperature" + String(temp));

obniz.wait(4000);//４秒待機

var DEVICE = "";//センサー名
var TEMP = temp;
var DATE = new Date().toLocaleString({ timeZone: 'Asia/Tokyo' });
var MESS = "Comfortable temperature";
var ID = "";//つけたい名前で良い

if (TEMP > 29) {
    MESS = "Beware of heat";
}
if (TEMP < 11) {
    MESS = "Beware of cold";
}

obniz.display.clear();
obniz.display.print(MESS);

obniz.wait(4000);//４秒待機

obniz.display.clear();
obniz.display.print("See you");

obniz.wait(2000);//2秒待機

obniz.display.clear();
led1.oﬀ();

msg.payload = [DEVICE, TEMP, DATE, MESS, ID];
return msg;