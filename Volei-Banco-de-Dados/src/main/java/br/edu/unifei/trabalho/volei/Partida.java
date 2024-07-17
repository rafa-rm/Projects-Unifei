package br.edu.unifei.trabalho.volei;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import javax.persistence.OneToOne;

import lombok.Data;

@Data
@Entity
public class Partida implements Serializable{
	private static final long serialVersionUID = -8713383417693767053L;
	@Id
	@GeneratedValue
	private int codigo;
	private String localidade;
	private int publico;
	@OneToOne
	private Equipe equipe1;
	@OneToOne
	private Equipe equipe2;
	@OneToOne
	private Equipe vencedor;
	@OneToOne
	private Estadio estadio;
	@OneToMany
	private List<SetDisputado> sets = new ArrayList<SetDisputado>();
}
