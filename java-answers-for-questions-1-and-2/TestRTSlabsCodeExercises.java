import org.junit.Test;

import jdk.jfr.Timestamp;

import static org.junit.Assert.assertEquals;

public class TestRTSlabsCodeExercises {
    

    @Test
    public void testElementsAboveAndBelowN() {

        int[] arr = {46,9,-23,0,-45,88,12};

        String string = RTSlabsCodeExercises.elementsAboveAndBelowN(arr, 0);
        assertEquals("above: 4, below: 2", string);
    }

    @Test 
    public void testRotateByN() {

        String string = RTSlabsCodeExercises.rotateByN("Pittsburgh Steelers", 3);
        assertEquals("ersPittsburgh Steel", string);
    }
}
