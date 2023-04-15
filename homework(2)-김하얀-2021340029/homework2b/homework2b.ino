
int si0=262;
int dow = 277;
int rae = 311;
int rae00 = 330;
int mi = 349;
int pa = 370;
int sol = 415;
int ra = 466;
int si=524;
int dow1 = 554;

int duration;

int melody[] = {
  mi, si, si, pa, mi, mi, si0, mi, mi, pa, mi,
  mi, si, si, pa, mi, mi, si0, mi, mi, pa, mi,
  mi, si, ra, mi, pa, rae, rae, ra, sol, dow,
  si0, dow, rae, mi, pa, sol, ra, si, ra, rae00
};

int noteDurations[] = {
  4,4,4,4,4,4,4,4,4,4,8, //1마디
  4,4,4,4,4,4,4,4,4,4,8, //2마디
  4,4,4,4,4,4,4,4,4,12, //2마디
  4,4,4,4,4,4,4,4,4,12, //2마디
};

void setup() {
  pinMode(8, OUTPUT);
}

void repeat(){
  for (int i = 0; i < sizeof(melody) / sizeof(melody[0]); i++) {
    duration = noteDurations[i]*120;
    tone(8, melody[i], duration);
    delay(duration);
  }
  delay(1000);  
}

void loop() {
  repeat();
  exit(0);
}
