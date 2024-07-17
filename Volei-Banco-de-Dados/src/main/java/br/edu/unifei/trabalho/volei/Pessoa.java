package br.edu.unifei.trabalho.volei;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.Id;

import lombok.Data;

@Data
@Entity
public abstract class Pessoa implements Serializable{
	private static final long serialVersionUID = -1781503031644113891L;
	@Id
	private String nome;
	private int altura;
	private float peso;
	private int idade;	
}