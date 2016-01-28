
public class Roster {
	
	private String name;
	private float wage;

	public Roster(String name, float wage){
		this.name = name;
		this.wage = wage;
	}
	
	public String getName(){
		return this.name;
	}
	public void setName(String name){
		this.name = name;
	}
	
	public float getWage(){
		return this.wage;
	}
	public void setWage(float wage){
		this.wage = wage;
	}
	
	class HourlyEmployee{
		private String manager;
		private String title;
		
		public HourlyEmployee(String manager, String title){
			this.manager = manager;
			this.title = title;
		}
		public String getManager(){
			return this.manager;
		}
		public void setManager(String manager_name){
			this.manager = manager_name;
		}
		public String getTitle(){
			return this.title;
		}
		public void setTitle(String set_title){
			this.title = set_title;
		}
		
	}
	
}
