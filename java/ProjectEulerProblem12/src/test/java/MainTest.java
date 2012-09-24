import junit.framework.Assert;
import org.junit.Test;

public class MainTest {

    @Test
    public void testGetTriangle() {
        Assert.assertEquals(28, Main.getTriangle(7));
    }

    @Test
    public void testGetNumberOfDivisors(){
        Assert.assertEquals(6, Main.getNumberOfDivisors(28));
    }

}
