package br.edu.unifei.trabalho.volei;

import java.io.Serializable;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToOne;

import lombok.Data;

@Data
@Entity
public class SetDisputado implements Serializable{
	private static final long serialVersionUID = 5489522755153963651L;
	@Id
	@GeneratedValue
	private int codigo;
	private int duracaoMinutos;
	@OneToOne
	private Equipe vencedor;
}
