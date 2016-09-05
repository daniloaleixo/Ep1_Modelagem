

public class mru extends Particle {
	static double y, v, t, y0, t0;
	static double dt = 0;
	
	public mru(double v, double y0, double t0) {
		this.v = v;
		this.y0 = y0;
		this.t0 = t0;
	}

	public void step() {
		y = y+v*dt;
		t = t+dt;
	}

	public double Position(double y0, double dt, double v) {
		return y0+v*dt;
	}
	
	public double analyticVelocity() {
		return 0;
	}

	public double analyticPosition() {
		return 0;
	}

	public static void main(String[] args) {
		mru teste = new mru(3, 0, 0);
		System.out.println("distancia percorida " + teste.Position(teste.y0, 10, teste.v));	
	}
}
