package ru.brxq;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

    private static final DecimalFormat df2 = new DecimalFormat("#.##");

    public static void main(String[] args) {
	    double firstBorder;
	    double secondBorder;
	    double root;
	    double e;
	    int counter = 1;

        Scanner scanner = new Scanner(System.in);
        firstBorder = Double.parseDouble(scanner.nextLine());
        secondBorder = Double.parseDouble(scanner.nextLine());
        e = Double.parseDouble(scanner.nextLine());
        root = firstBorder;

        if ( expression(firstBorder) * expression(secondBorder) < 0) {

            if (expression(root) * expressionDerDer(root) > 0) {
                root = secondBorder;
            }

            while (Math.abs(expression(root) / expressionDer(root)) > e) {
                root -= expression(root) / expressionDer(root);
                counter += 1;
            }

            System.out.println("Root equals " + df2.format(root) + " found in " + counter + " steps");
            System.out.println("Reenter bonds? Space for exit");

        }else System.out.println("No root in this borders");

    }

    public static double expression(double x){
        return 1.4*Math.cos(0.6*x - 0.5) - 0.4*x*x*x;
    }
    public static double expressionDer(double x){
        return -1.2*x*x - 0.84*Math.sin(0.6*x - 0.5);
    }
    public static double expressionDerDer(double x){
        return -2.4*x - 0.504*Math.cos(0.6*x - 0.5);
    }
}
