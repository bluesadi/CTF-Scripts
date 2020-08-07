import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Arrays;

public class temp{

    public static void main(String args[]) throws Throwable{
        File file = new File("output.enc");
        InputStream in = new FileInputStream(file);
        int[] b = new int[100];
        int ptr = 0;
        while((b[ptr++] = in.read()) != -1);
        System.out.println(Arrays.toString(b));
    }

}