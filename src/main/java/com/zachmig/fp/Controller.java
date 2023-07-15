package com.zachmig.fp;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * Rest Controller which will handle get requests containing a food name
 * 	and respond with a JSON containing its neighbors
 * Requests should be formatted as in this example: localhost:8080/food?name=Apple
 * @author zmigliorini@gmail.com
 *
 */
@RestController
public class Controller {
	@Autowired
	private FoodRepository foodRepo;
	
	
	/**
	 * 
	 * Method to process HTTP GET requests that end in /country?name=COUNTRYNAME
	 * 
	 * @param name country name as HTTP GET parameter
	 * 	When provided by client, whitespace in between words should be replaced by underlines 
	 * 	and this method will expect and handle underlines.
	 * @return a Country object for JSON serialization, or NULL if there is 
	 * 	a problem creating the object or locating the record in DB.
	 */
	@GetMapping(
			value = "/food"
	)
	@CrossOrigin
	public List<String> getFoods(@RequestParam(value="name") String name) { 
		
		return foodRepo.findByName(name.replace("_", " ").trim());
				
	}
	
}
