<!DOCTYPE html>
<html>

<head>
	<title>Life Path Number</title>
	<meta charset="UTF-8" />
</head>

<body>
  

	<script>
	var date = "19971101";
var birthday_digitlist = [];
var soulNumber_list = [];
var lifeNumber_list = [];
var lifeNumber = 0;

function BirthdayCal(numbers){
    birthday_digitlist = (numbers.split(""));
    var date = birthday_digitlist;
    document.write(date);
    var year = date[0] + date[1] + date[2] + date[3];
    var month = date[4] + date[5];
    var day = date[6] + date[7];

    return document.write("The birthday of the person is " + year + "-" + month + "-" + day);
    
}

function HoroscopeCal(numbers){
    var date = birthday_digitlist;
    var month = date[4] + date[5];
    var day = (+(date[6] + date[7]));
    var sign = "";

    if (month == "12"){
        if (day < 23){
            sign = "Sagittarius";
            soulNumber_list = 9;
        }
        else{
            sign = "Capricorn";
            soulNumber_list = [10,1];
        }
    }
    if (month == "01"){
        if (day < 21){
            sign = "Capricorn";
            soulNumber_list = [10,1];
        }
        else{
            sign = "Aquarius";
            soulNumber_list = [11,2];
        }
    }
    if (month == "02"){
        if (day < 20){
            sign = "Aquarius";
            soulNumber_list = [11,2];
        }
        else{
            sign = "Pisces";
            soulNumber_list = [12,3];
        }
    }
    if (month == "03"){
        if (day < 22){
            sign = "Pisces";
            soulNumber_list = [12,3];
        }
        else{
            sign = "Aries";
            soulNumber_list = 1;
        }
    }
    if (month == "04"){
        if (day < 21){
            sign = "Aries";
            soulNumber_list = 1;
        }
        else{
            sign = "Taurus";
            soulNumber_list = 2;
        }
    }
    if (month == "05"){
        if (day < 22){
            sign = "Taurus";
            soulNumber_list = 2;
        }
        else{
            sign = "Gemini";
            soulNumber_list = 3;
        }
    }
    if (month == "06"){
        if (day < 22){
            sign = "Gemini";
            soulNumber_list = 3;
        }
        else{
            sign = "Cancer";
            soulNumber_list = 4;
        }
    }
    if (month == "07"){
        if (day < 24){
            sign = "Cancer";
            soulNumber_list = 4;
        }
        else{
            sign = "Leo";
            soulNumber_list = 5;
        }
    }
    if (month == "08"){
        if (day < 24){
            sign = "Leo";
            soulNumber_list = 5;
        }
        else{
            sign = "Virgo";
            soulNumber_list = 6;
        }
    }
    if (month == "09"){
        if (day < 24){
            sign = "Virgo";
            soulNumber_list = 6;
        }
        else{
            sign = "Libra";
            soulNumber_list = 7;
        }
    }
    if (month == "10"){
        if (day < 24){
            sign = "Libra";
            soulNumber_list = 7;
        }
        else{
            sign = "Scorpio";
            soulNumber_list = 8;
        }
    }
    if (month == "11"){
        if (day < 23){
            sign = "Scorpio";
            soulNumber_list = 8;
        }
        else{
            sign = "Sagittarius";
            soulNumber_list = 9;
        }
    }
    return document.write("<br><br>Horoscope Sign: " + sign + "<br><br>Soul Number: " + soulNumber_list);
}

function LifeNumberCal(numbers){
    var remain = 0;
    var digit = 1;
    var sum = 0;
    
    //Top code is to split the digit individually and add into one sum      
    while (numbers >= 10){
       remain = numbers % digit;
       numbers = numbers - remain;
       sum = sum + (remain / digit * 10);

        //Bottom code is to check if sum > 10, repeat loop till less than 10, reset all parameter
        if (numbers == 0 && sum >= 10){
            digit = 1;
            numbers = sum;
            lifeNumber_list.push(numbers);
            sum = 0;
          
        }
        digit *= 10;
        lifeNumber = sum;
    }
    return document.write("<br><br>Total Number breakdown: " + lifeNumber_list + "<br><br>Life Path Number: " + sum); 
}

BirthdayCal(date);
HoroscopeCal(date);
LifeNumberCal(date);
	</script>

	
	  <p><br>Created by Jirukouya</p>
</body>

</html>