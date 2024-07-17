package br.edu.unifei.trabalho.volei;

import java.io.Serializable;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToOne;

import lombok.Data;

@Data
@Entity
public class Estadio implements Serializable{
	private static final long serialVersionUID = 4282907271899002718L;
	@Id
	private String nome;
	private int capacidadeMaxima;
	@OneToOne
	private Torcida torcida1;
	@OneToOne
	private Torcida torcida2;
}
