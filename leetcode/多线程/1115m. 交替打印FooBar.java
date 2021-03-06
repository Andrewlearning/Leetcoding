"""
我们提供一个类：
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。
请设计修改程序，以确保 "foobar" 被输出 n 次。


示例 1:
输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
"""
class FooBar {
    private int n;
    private static int flag = 0;
    private static Object lock = new Object();

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            synchronized (lock) {
                while (flag != 0) {
                    lock.wait();
                }
                printFoo.run();
                flag = 1;
                lock.notifyAll();
            }

        }
    }

    public void bar(Runnable printBar) throws InterruptedException {

        for (int i = 0; i < n; i++) {
            synchronized (lock) {
                while (flag != 1) {
                    lock.wait();
                }
                printBar.run();
                flag = 0;
                lock.notifyAll();
            }

        }
    }
}

"""
思路沿用1114的思路
"""