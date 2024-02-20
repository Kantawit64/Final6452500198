*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;
std_msgs::Int16 sensorData;


void control_LED( const std_msgs::Int16 & cmd_msg )
{
  int value = cmd_msg.data;
  digitalWrite(13, value);   // blink the led
}

void control_turtle()
{
}

ros::Subscriber<std_msgs::Int16> sub("Topic_led", &control_LED );
ros::Publisher pub ("Topic_led", &sensorData);
ros::Subscriber<std_msgs::Int16> sub("turtle1/cmd_vel", &control_LED );

void setup()
{ 
  pinMode(13, OUTPUT);//led
  pinMode(3, INPUT);//input
  pinMode(4, INPUT);
  pinMode(5, INPUT);
  
  
  nh.initNode();
  nh.subscribe(sub);
  nh.advertise(pub);
}


void loop()
{  
  sensorData.data = digitalRead(3);
  pub.publish(&sensorData);
  nh.spinOnce();
  delay(1);
}
