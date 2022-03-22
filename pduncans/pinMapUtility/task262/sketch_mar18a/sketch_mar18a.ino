int delayT = 1000;
int pin = 20;
void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
  Serial1.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(pin, HIGH);
  delay(delayT);
  digitalWrite(pin, LOW);
  delay(delayT);
  Serial1.println("test");
}
