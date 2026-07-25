public class Lasagna {
    int time = 40;
    // TODO: define the 'expectedMinutesInOven()' method
    public int expectedMinutesInOven(){
        return time;
    }
    // TODO: define the 'remainingMinutesInOven()' method
    public int remainingMinutesInOven(int timeInOven){
        return expectedMinutesInOven()-timeInOven;
    } 
    // TODO: define the preparationTimeInMinutes()' method
    public int preparationTimeInMinutes(int layers){
        return 2*layers;
    }
    // TODO: define the 'totalTimeInMinutes()' method
    public int totalTimeInMinutes(int layers, int timeInOven){
        return timeInOven+preparationTimeInMinutes(layers);
    }
}
