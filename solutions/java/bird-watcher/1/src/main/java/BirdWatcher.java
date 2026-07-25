
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public static int[] getLastWeek() {
         return new int[] {0, 2, 5, 3, 7, 8, 4};
    }

    public int getToday() {
        return birdsPerDay[getLastWeek().length-1];
    }

    public void incrementTodaysCount() {
        birdsPerDay[getLastWeek().length-1] = getToday()+1;
    }

    public boolean hasDayWithoutBirds() {
        for(int i:birdsPerDay){
            if(i==0)
                return true;
        }
        return false;
    }

    public int getCountForFirstDays(int numberOfDays) {
        int count=0;
        int higherEnd = Math.min(numberOfDays, birdsPerDay.length);
        for(int i=0;i<higherEnd;i++){
            count+=birdsPerDay[i];
        }
        return count;
    }

    public int getBusyDays() {
        int busyDays=0;
        for(int i:birdsPerDay){
            if(i>=5) busyDays++;
        }
        return busyDays;
    }
}
