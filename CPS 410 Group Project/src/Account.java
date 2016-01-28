
public class Account {
	private String name;
	private String phone;
	private int custid;
	private String contactdate;
	private String estimatedate;
	private String bookdate;
	private float price;

	public Account(String name, String phone, int custid, String contactdate, String estimatedate, String bookdate, float price){
		this.name = name;
		this.phone = phone;
		this.custid = custid;
		this.contactdate = contactdate;
		this.estimatedate = estimatedate;
		this.bookdate = bookdate;
		this.price = price;
	}
	
	public String getCustName(){
		return this.name;
	}
	public void setCustName(String set_name){
		this.name = set_name;
	}
	
	public String getCustPhone(){
		return this.phone;
	}
	public void setCustPhone(String set_phone){
		this.phone = set_phone;
	}
	
	public int getCustId(){
		return this.custid;
	}
	public void setCustId(int set_custid){
		this.custid = set_custid;
	}
	
	public String getContactDate(){
		return this.contactdate;
	}
	public void setContactDate(String set_contactdate){
		this.contactdate = set_contactdate;
	}
	
	public String getEstimateDate(){
		return this.estimatedate;
	}
	public void setEstimateDate(String set_estimatedate){
		this.estimatedate = set_estimatedate;
	}
	
	public String getBookDate(){
		return this.bookdate;
	}
	public void setBookDate(String set_bookdate){
		this.bookdate = set_bookdate;
	}
	
	public float getPrice(){
		return this.price;
	}
	public void setPrice(float set_price){
		this.price = set_price;
	}
	
}
