import java.util.ArrayList;
import java.util.List;

public class Main implements ThreadListener {

    List<CalNum> res;
    CalNum largest;

    public Main() {
        new PrintThread().start();
        largest = new CalNum(1, 1, 1);
        long maxNum = (long) Math.pow(2, 16);
        List<Long> nums = new ArrayList<Long>();
        res = new ArrayList<CalNum>();

        for (long i = 1; i <= maxNum; i++) {
            nums.add(i);
        }

        for (long num : nums) {
            new CalThread(num, this).start();
        }
    }

    @Override
    public void done(CalNum calNum) {
        this.res.add(calNum);
        if (calNum.getNumberOfDivisors() > 500) {
            System.out.println("\n"+calNum);
            System.exit(0);
        }
    }

    public static long getTriangle(long num) {
        long tri = 0;
        for (long i = 1; i <= num; i++) {
            tri += i;
        }
        return tri;
    }

    public static long getNumberOfDivisors(long num) {
        long divs = 0;
        for (long i = 1; i < Math.sqrt(num); i++) {
            if(num % i == 0) {
                divs += 2;
            }
        }
        return divs;
    }

    public static void main(String[] args) {
        Main main = new Main();
    }

    class CalNum {
        long num, tri, div;
        public CalNum(long num, long tri, long div) {
            this.num = num;
            this.tri = tri;
            this.div = div;
        }

        public long getNumber() {
            return this.num;
        }

        public long  getTriangle() {
            return this.tri;
        }

        public long  getNumberOfDivisors() {
            return this.div;
        }

        @Override
        public String toString() {
            return "CalNum{" +
                    "num=" + num +
                    ", tri=" + tri +
                    ", div=" + div +
                    '}';
        }
    }

    class CalThread extends Thread {
        long num, tri, div;
        ThreadListener listener;
        public CalThread(long num, ThreadListener listener) {
            this.num = num;
            this.listener = listener;
        }

        public void run() {
            this.tri = getTriangle(this.num);
            this.div = getNumberOfDivisors(this.tri);
            this.listener.done(new CalNum(this.num, this.tri, this.div));
        }
    }

    class PrintThread extends Thread {
        public void run() {
            while(true) {
                System.out.print(".");
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();  //To change body of catch statement use File | Settings | File Templates.
                }
            }
        }
    }

}

/*
#! /usr/bin/env python

from clint.textui import progress, puts

def triangle(num):
    tri = 0
    for x in range(1, num+1):
        tri += x
    return tri

def get_divisors(num):
    divs = []
    for x in range(1, num+1):
        if num % x == 0:
            divs.append(x)
    return divs

def main():
    nums = range(1, 2**16)
    largest = 0
    first = 0
    for n in progress.bar(nums):
        len_div = len(get_divisors(triangle(n)))
        if len_div > largest:
            largest = len_div
            puts("[%d, %d, %d" % (n, triangle(n), largest))

if __name__ == '__main__':
    main()
 */
