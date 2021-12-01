var date = "01111997";
var birthday_digitlist = [];
var lifeNumber_list = [];
var lifeNumber = 0;

function BirthdayCal(numbers){
    birthday_digitlist.concat(numbers.split(""))
    date = birthday_digitlist



    return if (birthday_digitlist.length == 8){
      document.write("The birthday of the person is " + birthday_digitlist[0] + "-" + birthday_list[1] + "-" + birthday_list[2]);
    }
    
}

function lifeNumberCal(numbers){
    var remain = 0;
    var digit = 1;
    var sum = 0;
    
//=========Top code is to split the digit individually and add into one sum      
    while (numbers >= 10){
       remain = numbers % digit;
       numbers = numbers - remain;
       sum = sum + (remain / digit * 10);

  //=========Bottom code is to check if sum > 10, repeat loop till less than 10, reset all parameter
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
lifeNumberCal(date);
