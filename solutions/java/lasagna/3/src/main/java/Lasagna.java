public class Lasagna {
    int time = 40;
    public int expectedMinutesInOven(){
        return time;
    }
    public int remainingMinutesInOven(int timeInOven){
        return expectedMinutesInOven()-timeInOven;
    } 
    public int preparationTimeInMinutes(int layers){
        return 2*layers;
    }
    public int totalTimeInMinutes(int layers, int timeInOven){
        return timeInOven+preparationTimeInMinutes(layers);
    }
}
