import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;
public class BerkeleyAlgorithm{
public static void berkeleyAlgo(String servertime, String time1, String time2){
System.out.println("Server Clock   = " + servertime);
System.out.println("Clienr Clock1  = " + time1);
System.out.println("Clienr Clock2  = " + time2);
SimpleDateFormat sdf = new SimpleDateFormat("mm:ss");
try{
long s = sdf.parse(servertime).getTime();
long t1 = sdf.parse(time1).getTime();
long t2 = sdf.parse(time2).getTime();
long st1 = t1 - s;
System.out.println("t1 - s = " + st1 / 1000);
long st2 = t2 - s;
System.out.println("t1 - s = " + st2 / 1000);
long avg = (st1 + st2) / 2;
System.out.println(" (st1 + st2) / 2 = " + avg / 1000);
long adjserver = avg + s;
long adj_t1 = avg - st1;
long adj_t2 = avg - st2;
System.out.println(" t1 adjustment = " + adj_t1 / 1000);
System.out.println(" t2 adjustment = " + adj_t2 / 1000);
System.out.println(" Synchronized Server Clock = " + sdf.format (new Date(adjserver)));
System.out.println(" Synchronized Client1 Clock = " + sdf.format (new Date(t1 + adj_t1)));
System.out.println(" Synchronized Client2 Clock = " + sdf.format (new Date(t2 + adj_t2)));
} catch (ParseException e) {
e.printStackTrace();
}
}
public static void main(String[] args) {
Scanner scanner = new Scanner(System.in);
System.out.print("Enter Server Time (mm:ss): ");
String servertime = scanner.nextLine();
System.out.print("Enter Client 1 Time (mm:ss): ");
String time1 = scanner.nextLine();
System.out.print("Enter Client 2 Time (mm:ss): ");
String time2 = scanner.nextLine();
berkeleyAlgo(servertime, time1, time2);
}
}

